library(tidyverse)
library(lubridate)

d <- read.csv("~/Downloads/seg_model_batch_run_data.csv")

####### Basic line plot
###

ggplot(d) +
  geom_line(aes(X, y=Pct.Happy, color="Happiness", ), size = 2) +
  geom_line(aes(X, y=Avg.pct.similar.neighbors, color="Neighbor similarity"), size = 2) +
  scale_x_continuous("Model Time Step", breaks=seq(0, 300, 25)) +
  scale_y_continuous("Percent", breaks=seq(0, 100, 10), limits = c(0, 105)) +
  labs(title="Happiness and Similarity \nover model run") +
  scale_color_manual(name = "Proportions",
                     values = c("Happiness" = "black",
                                "Neighbor similarity" = "gray50")) +
  theme_bw() +
  theme(legend.position="bottom",
        text = element_text(size = 18),
        legend.text = element_text(size = 18),
        legend.title = element_text(size = 20),
        plot.subtitle=element_text(size=16, face="italic", color="grey40"))

####### Getting ready for fancier plot
###

# tidy and reshape the data
seg_batch <- d %>% 
  group_by(intolerance) %>%
  mutate(avg_similar = mean(Avg.pct.similar.neighbors, na.rm = TRUE),
         avg_similar_e = mean(Avg.pct.similar.neighbors..count.empty., na.rm = TRUE))

# plot the data
ggplot(seg_batch) + 
  geom_jitter(aes(intolerance,  y=Avg.pct.similar.neighbors, color="Neighbors"), 
              width = 0.005, size = 4) +
  geom_jitter(aes(intolerance,  y=Avg.pct.similar.neighbors..count.empty., color="Neighbors \nw/empty"), 
              width = 0.005, size = 4, shape=18) +
  geom_point(aes(intolerance, y=avg_similar, color="Avg"), size = 6.5) +
  geom_point(aes(intolerance, y=avg_similar_e, color="Avg \nw/empty"), shape=18, size = 6.5) +
  scale_x_continuous("Preferred % similar neighbors",  breaks=seq(0, 1, 0.125), labels = scales::percent) +
  scale_y_continuous("Proportion of smilar neighbors", breaks=seq(45, 70, 5)) +
  labs(title="Agent neigbhorhood similarity", 
       caption="Note: point position jittered for interpretability \n Similarity calculated using only neighboring agents (Avg) \nand calculated including empty cells (Avg w/empty).") +
  scale_color_manual(name = "Neighborhood \ntypes", 
                     values = c("Neighbors" = "grey",
                                "Avg" = "black",
                                "Neighbors \nw/empty" = "rosybrown3",
                                "Avg \nw/empty" = "red4") ) + 
  theme_bw() +
  theme(legend.position="bottom", 
        text = element_text(size = 17),
        axis.title = element_text(size = 21),  
        legend.text = element_text(size = 17),
        legend.title = element_text(size = 21),
        plot.caption = element_text(size=14), 
        plot.subtitle=element_text(size=16, face="italic", color="grey40")) + 
  guides(title.position = "top", label.position = "bottom",
         col = guide_legend(nrow = 2, byrow = TRUE))
