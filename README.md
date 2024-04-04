# MACSS 40550 ABM
 ABM course in MACSS program taught Spring 2024. 

 Each week has a separate folder, skill, and model / component that we'll cover. Readings are below, including models / code are here. 

 Textbook: You MAY find the following text helpful, but note that it covers NetLogo instead of using Python: Agent-Based and Individual-Based Modeling: A Practical Introduction, Second Edition. ISBN: 0691190836

 Other: you might want to skim through this [intro to Mesa](https://mesa.readthedocs.io/en/stable/tutorials/intro_tutorial.html).


|Week  |Skill  focus / Substantive  focus   |Goal  for week.   |Classic  model  |Readings|
|-------|---------------------------------------|---------------------|-----------------|----------------|
|**week 1**   | Intro  & background | Understand  basics and some of greatest hits  |[Game  of life](https://playgameoflife.com/) / Wolfram |Textbook  Ch 1  | |
|  |  |  |   |Kazil,  Jackie, David Masad, and Andrew Crooks. 2020. [“Utilizing Python for  Agent-Based Modeling: The Mesa Framework.”](https://link.springer.com/chapter/10.1007/978-3-030-61255-9_30) In Social, Cultural, and  Behavioral Modeling, Lecture Notes in Computer Science, eds. Robert Thomson  et al. Cham: Springer International Publishing, 308–17.  |
|  |  |  |   |Epstein, Joshua M. 2008. “Why Model?” https://jasss.soc.surrey.ac.uk/11/4/12.html  (October 3, 2022).  |
| **Thursday** |  |  |   |Elster, Jon. (1998) [“A Plea for Mechanisms.”](https://edisciplinas.usp.br/pluginfile.php/7576776/mod_folder/content/0/Textos/Hedstr%C3%B6m%20and%20Swedberg%2C%20Social%20Mechanisms%20-%20an%20analytical%20approach%20to%20social%20theory.pdf?forcedownload=1) In Peter Hedström and Richard Swedberg (eds.), Social Mechanisms: An Analytical Approach to Social Theory (New York: Cambridge University Press), ch. 3. |
|  |  |  |   |Norling, Emma et al (2013). [“Informal Approaches to Developing Simulation Models.”](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=2525cbe4d1c32587100ade7a8ab0338e5015b896) Chapter 4 of Simulating Social Complexity |
|**week 2**   |Agents  & Initializing  |Create  new agent type (how??) OR initialize the world differently   |Schelling  | Schelling,  Thomas C. 1969. [“Models of Segregation.”](https://www.jstor.org/stable/1823701) The American Economic Review 59(2):  488–93. |
|  |  |  |  | Silver, Daniel et al (2021). [“Venues and segregation: A revised Schelling model.”](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0242611) PLoS One, 16(1) |
|  |  |  |   |Müller,  Birgit et al. 2013. [“Describing Human Decisions in Agent-Based Models –  ODD + D, an Extension of the ODD Protocol.”](https://www.sciencedirect.com/science/article/pii/S1364815213001394) Environmental Modelling  & Software 48: 37–48.   |
|**week 3**   |Emergence,  parameters, & visualizations  |Add additional  parameter value |Boids  / Flocking   |Grimm,  Volker et al. 2005. [“Pattern-Oriented Modeling of Agent-Based Complex  Systems: Lessons from Ecology.”](https://www.science.org/doi/10.1126/science.1116681) Science 310(5750): 987–91.   |
|  |  |  |[Ants  (brief)](https://ccl.northwestern.edu/netlogo/models/Ants) |Thompson, W. A., Vertinsky, I., & Krebs, J. R. (1974). [The Survival Value of Flocking in Birds: A Simulation Model. Journal of Animal Ecology](https://www.jstor.org/stable/3537) , 43(3), 785–820. https://doi.org/10.2307/3537    |
|  |  |  |   |[Netlogo web app of flocking](https://www.netlogoweb.org/launch#http://ccl.northwestern.edu/netlogo/models/models/Sample%20Models/Biology/Flocking.nlogo) | Reynolds, Craig (1987). ["Flocks, herds and schools: A distributed behavioral model"](https://team.inria.fr/imagine/files/2014/10/flocks-hers-and-schools.pdf). Proceedings of the 14th annual conference on Computer graphics and interactive techniques. Association for Computing Machinery. pp. 25–34. |
|  |  |  |   |Ch 8  from textbook  |
|**week 4**   |Sensing  / Environment, visualization / DataCollector   |Add /  change value of environment  |Schelling    |Crooks, Andrew T., and Christian J. E. Castle.  2012. [“The Integration of Agent-Based Modelling and Geographical Information  for Geospatial Simulation.”](https://link.springer.com/chapter/10.1007/978-90-481-8927-4_12) In Agent-Based Models of Geographical Systems,  eds. Alison J. Heppenstall, Andrew T. Crooks, Linda M. See, and Michael  Batty. Dordrecht: Springer Netherlands, 219–51.  https://doi.org/10.1007/978-90-481-8927-4_12 (October 3, 2022).   |
|  |  |  |  Greedy  cows (brief)  |Jordan, René, Mark Birkin, and Andrew Evans. 2012. [“Agent-Based  Modelling of Residential Mobility, Housing Choice and Regeneration.”](https://link.springer.com/chapter/10.1007/978-90-481-8927-4_25) In  Agent-Based Models of Geographical Systems, eds. Alison J. Heppenstall,  Andrew T. Crooks, Linda M. See, and Michael Batty. Dordrecht: Springer  Netherlands, 511–24. https://doi.org/10.1007/978-90-481-8927-4_25 |
|  |  |  | preview  Wolf / sheep  | [Mesa source code behind Data Collector](https://mesa.readthedocs.io/en/stable/_modules/datacollection.html)  |
|  |  |  |   |[Mesa  guide to Data Collector](https://mesa.readthedocs.io/en/stable/apis/datacollection.html) |
|  |  |  |   |*optional*: Groff, Elizabeth R.,  Shane D. Johnson, and Amy Thornton. 2019. [“State of the Art in Agent-Based  Modeling of Urban Crime: An Overview.”](https://link.springer.com/article/10.1007/s10940-018-9376-y) Journal of Quantitative Criminology  35(1): 155–93. |
|**week 5**   |Scheduling  & Updating  |Goal:  change the updating scheme of popular model|PD  Grid  |Comer,  Kenneth W., and Andrew G. Loerch. 2013. “The Impact of Agent Activation on  Population Behavior in an Agent-Based Model of Civil Revolt.” Procedia  Computer Science 20: 183–88.  |
|  |  |  |   |Alizadeh,  Meysam, and Claudio Cioffi-Revilla. “Activation Regimes in Opinion Dynamics:  Comparing Asynchronous Updating Schemes.” : 22.|
|**week 6**   |Docking | Export  model data |Proposal  workshop  |(revisit)  Comer, Kenneth W., and Andrew G. Loerch. 2013. “The Impact of Agent  Activation on Population Behavior in an Agent-Based Model of Civil Revolt.”  Procedia Computer Science 20: 183–88.|
|**week 7**   |Analysis  / YAAWN  | Critical  re-evaluation of model|Wolf  / sheepRumor  Mill (mention)   |O’Sullivan,  David et al. 2016. “Strategic Directions for Agent-Based Modeling: Avoiding  the YAAWN Syndrome.” Journal of Land Use Science 11(2): 177–87. |
|**week 8**   |Extensions  / Complications  |  |(student submissions)   |Sun,  Zhanli et al. 2016. “Simple or Complicated Agent-Based Models? A Complicated  Issue.” Environmental Modelling & Software 86: 56–67.Lamperti,  Francesco, Andrea Roventini, and Amir Sani. 2018. “Agent-Based Model  Calibration Using Machine Learning Surrogates.” Journal of Economic  Dynamics and Control 90: 366–89. |
|**week 9**   |(wrap) |  | Demos  | |

*Some readings from David Peterson's suggestions -- thanks!*
