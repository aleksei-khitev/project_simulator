# Simulation Results
Simulation count: **100**
## Total Profit for Year:
**Base Example**<br/>$$
90.71*R_{f/d} + 113.39*R_{df/d} + 22.68*P_{tdf/d} - 170,891 - C_{others}
$$<br/>**With IT Org**<br/>$$
136.05*R_{f/d} + 68.03*R_{df/d} + 22.68*P_{tdf/d} - 170,909 - C_{others}
$$<br/>**With Monitoring**<br/>$$
90.78*R_{f/d} + 113.48*R_{df/d} + 22.7*P_{tdf/d} - 170,645 - C_{others}
$$<br/>**All Improvements**<br/>$$
136.18*R_{f/d} + 68.09*R_{df/d} + 22.7*P_{tdf/d} - 170,642 - C_{others}
$$<br/>
### Abbreviations
$R_{{f/d}}$ - Average revenue from a day of new feature development<br/>$R_{{df/d}}$ - Average revenue from a day of fixing defects<br/>$R_{{tdf/d}}$ - Average revenue from a day of improving application by fixing tech depth<br/>C_{{others}} - Other costs<br/><br/>**Revenue from new feature development** inreases sales conversion rate, retention and feasibility of price increase<br/>**Revenue from fixing defects** decreases churn rate and reputational losses<br/>**Revenue from fixing tech depth** increases development speed, probability of occurrence of new defects 
### Cost Description
#### Total cost
| Simulation | Value |
| --- | --- |
| Base Example | 170,891.06 |
| With IT Org | 170,908.97 |
| With Monitoring | 170,644.69 |
| All Improvements | 170,642.26 |

#### Total cost contains:
| Simulation | Total salary spent on<br/>non profit activities | Down time cost | Total salary spent on<br/>profit activities |
| --- | --- |--- |--- |
| Base Example | 15,113.34 | 7,305.3 | 148472.42 |
| With IT Org | 15,115.04 | 7,331.4 | 148462.53 |
| With Monitoring | 15,066.75 | 6,983.64 | 148594.3 |
| All Improvements | 15,066.34 | 6,980.4 | 148595.52 |

#### Total salary spent on non profit activities contains:
| Simulation | Total salary spent on meetings | Total salary spent on troubleshooting | Total salary spent on release |
| --- | --- |--- |--- |
| Base Example | 9,835.2 | 55.74 | 5222.4 |
| With IT Org | 9,835.2 | 57.44 | 5222.4 |
| With Monitoring | 9,835.2 | 9.15 | 5222.4 |
| All Improvements | 9,835.2 | 8.74 | 5222.4 |

#### Down time contains:
| Simulation | Downtime because of release (hours) | Downtime because of troubles (hours) |
| --- | --- |--- |
| Base Example | 32.0 | 1.82 |
| With IT Org | 32.0 | 1.94 |
| With Monitoring | 32.0 | 0.33 |
| All Improvements | 32.0 | 0.32 |

### Troubles in the year:
| Simulation | Service errors because of lack of server's disk space | Error because of some service down in the chain of invocations |
| --- | --- | --- |
| Base Example | 1.36 | 2.38 |
| With IT Org | 1.47 | 2.14 |
| With Monitoring | 0 | 2.26 |
| All Improvements | 0 | 2.16 |

### Time Spent for Year:
| Simuation | Spent on<br/>working with feature | Spent on<br/>working with feature | Spent on<br/>technical depth fixing | Spent on meetings | Spent on troubleshooting | Spent on release |
| --- | --- | --- | --- | --- | --- | --- |
| Base Example | 43,540.3 |54,425.38 |10,885.08 |7,200.0 |109.25 |3,840.0 |
| With IT Org | 65,306.1 |32,653.05 |10,884.35 |7,200.0 |116.5 |3,840.0 |
| With Monitoring | 43,576.04 |54,470.05 |10,894.01 |7,200.0 |19.9 |3,840.0 |
| All Improvements | 65,364.6 |32,682.3 |10,894.1 |7,200.0 |19.0 |3,840.0 |
