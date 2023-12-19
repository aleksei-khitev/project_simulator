# Simulation Results

Simulation count: **100**

## Total Profit for Year:

**Base Example**

$ 90.21*R_{f/d} + 112.76*R_{df/d} + 22.55*P_{tdf/d} - 179,790 - C_{others} 
$

**With IT Org**<br/>$ 135.63*R_{f/d} + 67.82*R_{df/d} + 22.61*P_{tdf/d} - 176,189 - C_{others}$

**With Monitoring**

$ 90.28*R_{f/d} + 112.86*R_{df/d} + 22.57*P_{tdf/d} - 179,542 - C_{others}$

**All Improvements**

$ 135.72*R_{f/d} + 67.86*R_{df/d} + 22.62*P_{tdf/d} - 175,988 - C_{others}$

### Abbreviations

$R_{{f/d}}$ - Average revenue from a day of new feature development<br/>$R_{{df/d}}$ - Average revenue from a day of fixing defects<br/>$R_{{tdf/d}}$ - Average revenue from a day of improving application by fixing tech depth<br/>C_{{others}} - Other costs<br/><br/>**Revenue from new feature development** inreases sales conversion rate, retention and feasibility of price increase<br/>**Revenue from fixing defects** decreases churn rate and reputational losses<br/>**Revenue from fixing tech depth** increases development speed, probability of occurrence of new defects 

### Cost Description

#### Total cost

| Simulation       | Value      |
| ---------------- | ---------- |
| Base Example     | 179,790.24 |
| With IT Org      | 176,189.22 |
| With Monitoring  | 179,542.25 |
| All Improvements | 175,987.81 |

#### Total cost contains:

| Simulation       | Total salary spent on<br/>non profit activities | Down time cost | Total salary spent on<br/>profit activities |
| ---------------- | ----------------------------------------------- | -------------- | ------------------------------------------- |
| Base Example     | 24,831.47                                       | 7,304.4        | 147654.36                                   |
| With IT Org      | 20,937.19                                       | 7,249.5        | 148002.52                                   |
| With Monitoring  | 24,786.06                                       | 6,978.24       | 147777.94                                   |
| All Improvements | 20,899.12                                       | 6,986.52       | 148102.17                                   |

#### Total salary spent on non profit activities contains:

| Simulation       | Total salary spent on meetings | Total salary spent on troubleshooting | Total salary spent on release |
| ---------------- | ------------------------------ | ------------------------------------- | ----------------------------- |
| Base Example     | 19,555.2                       | 53.87                                 | 5222.4                        |
| With IT Org      | 15,667.2                       | 47.59                                 | 5222.4                        |
| With Monitoring  | 19,555.2                       | 8.46                                  | 5222.4                        |
| All Improvements | 15,667.2                       | 9.52                                  | 5222.4                        |

#### Down time contains:

| Simulation       | Downtime because of release (hours) | Downtime because of troubles (hours) |
| ---------------- | ----------------------------------- | ------------------------------------ |
| Base Example     | 32.0                                | 1.82                                 |
| With IT Org      | 32.0                                | 1.56                                 |
| With Monitoring  | 32.0                                | 0.31                                 |
| All Improvements | 32.0                                | 0.34                                 |

### Troubles in the year:

| Simulation       | Service errors because of lack of server's disk space | Error because of some service down in the chain of invocations |
| ---------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| Base Example     | 1.45                                                  | 2.08                                                           |
| With IT Org      | 1.25                                                  | 2.19                                                           |
| With Monitoring  | 0                                                     | 2.11                                                           |
| All Improvements | 0                                                     | 2.41                                                           |

### Time Spent for Year:

| Simuation        | Spent on<br/>working with feature | Spent on<br/>working with defects | Spent on<br/>technical depth fixing | Spent on meetings | Spent on troubleshooting | Spent on release |
| ---------------- | --------------------------------- | --------------------------------- | ----------------------------------- | ----------------- | ------------------------ | ---------------- |
| Base Example     | 43,300.4                          | 54,125.5                          | 10,825.1                            | 7,800.0           | 109.0                    | 3,840.0          |
| With IT Org      | 65,103.75                         | 32,551.88                         | 10,850.62                           | 7,560.0           | 93.75                    | 3,840.0          |
| With Monitoring  | 43,336.64                         | 54,170.8                          | 10,834.16                           | 7,800.0           | 18.4                     | 3,840.0          |
| All Improvements | 65,147.58                         | 32,573.79                         | 10,857.93                           | 7,560.0           | 20.7                     | 3,840.0          |
