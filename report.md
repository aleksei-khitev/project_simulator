# Simulation Results
Simulation count: **100**
## Total Profit for Year:
**Base Example**<br/>$$
90.71270833333332*R_{f/d} + 113.39087500000001*R_{df/d} + 22.678166666666666*P_{tdf/d} - 170,877.98 - C_{others}
$$<br/>**With IT Org**<br/>$$
136.0515625*R_{f/d} + 68.02579166666666*R_{df/d} + 22.675250000000002*P_{tdf/d} - 170,916.37 - C_{others}
$$<br/>**With Monitoring**<br/>$$
90.78408333333333*R_{f/d} + 113.48010416666666*R_{df/d} + 22.696020833333332*P_{tdf/d} - 170,642.53 - C_{others}
$$<br/>**All Improvements**<br/>$$
136.1765*R_{f/d} + 68.08825*R_{df/d} + 22.696083333333334*P_{tdf/d} - 170,641.72 - C_{others}
$$<br/>
### Abbreviations
$R_{{f/d}}$ - Average revenue from a day of new feature development<br/>$R_{{df/d}}$ - Average revenue from a day of fixing defects<br/>$R_{{tdf/d}}$ - Average revenue from a day of improving application by fixing tech depth<br/>C_{{others}} - Other costs<br/><br/>**Revenue from new feature development** inreases sales conversion rate, retention and feasibility of price increase<br/>**Revenue from fixing defects** decreases churn rate and reputational losses<br/>**Revenue from fixing tech depth** increases development speed, probability of occurrence of new defects 
### Cost Description
#### Total cost
| Simulation | Value |
| --- | --- |
| Base Example | 170,877.98 |
| With IT Org | 170,916.37 |
| With Monitoring | 170,642.53 |
| All Improvements | 170,641.72 |

#### Total cost contains:
| Simulation | Total salary spent on<br/>non profit activities | Down time cost | Total salary spent on<br/>profit activities |
| --- | --- |--- |--- |
| Base Example | 15,110.32 | 7,289.1 | 148478.56 |
| With IT Org | 15,117.4 | 7,339.5 | 148459.46 |
| With Monitoring | 15,066.39 | 6,980.76 | 148595.39 |
| All Improvements | 15,066.25 | 6,979.68 | 148595.8 |

#### Total salary spent on non profit activities contains:
| Simulation | Total salary spent on meetings | Total salary spent on troubleshooting | Total salary spent on release |
| --- | --- |--- |--- |
| Base Example | 9,835.2 | 52.72 | 5222.4 |
| With IT Org | 9,835.2 | 59.8 | 5222.4 |
| With Monitoring | 9,835.2 | 8.79 | 5222.4 |
| All Improvements | 9,835.2 | 8.65 | 5222.4 |

#### Down time contains:
| Simulation | Downtime because of release (hours) | Downtime because of troubles (hours) |
| --- | --- |--- |
| Base Example | 32.0 | 1.75 |
| With IT Org | 32.0 | 1.98 |
| With Monitoring | 32.0 | 0.32 |
| All Improvements | 32.0 | 0.31 |

### Troubles in the year:
| Simulation | Service errors because of lack of server's disk space | Error because of some service down in the chain of invocations |
| --- | --- | --- |
| Base Example | 1.45 | 2.11 |
| With IT Org | 1.61 | 2.46 |
| With Monitoring | 0 | 2.22 |
| All Improvements | 0 | 2.11 |

### Time Spent for Year:
| Simuation | Spent on<br/>working with feature | Spent on<br/>working with feature | Spent on<br/>technical depth fixing | Spent on meetings | Spent on troubleshooting | Spent on release |
| --- | --- | --- | --- | --- | --- | --- |
| Base Example | 43,542.1 |54,427.62 |10,885.52 |7,200.0 |104.75 |3,840.0 |
| With IT Org | 65,304.75 |32,652.38 |10,884.12 |7,200.0 |118.75 |3,840.0 |
| With Monitoring | 43,576.36 |54,470.45 |10,894.09 |7,200.0 |19.1 |3,840.0 |
| All Improvements | 65,364.72 |32,682.36 |10,894.12 |7,200.0 |18.8 |3,840.0 |
