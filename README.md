<h1 align="center">
  <br>
  <a href="http://autonom.io"><img src="https://raw.githubusercontent.com/autonomio/pandemik/master/assets/logo.png" alt="Pandemik" width="250"></a>
  <br>
</h1>

<h3 align="center">Behavior Change and Mitigation Simulation</h3>

<p align="center">
  <a href="#what">what?</a> •
  <a href="#why">why?</a> •
  <a href="#how">how?</a> •
  <a href="#start-simulating">start simulating</a> •
  <a href="https://autonom.io">About Autonomio</a> •
  <a href="https://github.com/autonomio/ICUSIM/issues">Issues</a> •
  <a href="#License">License</a>
</p>
<hr>
<p align="center">
Pandemik is an end-to-end pipeline for simulating behavior change and mitigation effects on <b>public health, economic, and psychological</b> outcomes**.</p>
<hr>

### What?

Pandemik helps researchers and decision makers answer the question **_"which behavior changes and mitigations are most likely to yield favorable public health, economic, and psychological outcomes"_**.

Pandemik brings together gold standard behavior change, epidemic, and capacity modelling capabilities into an end-to-end simulation pipeline. The modelling pipeline connects behavior change and mitigation actions with public health, economic, and psychological outcomes. 

A [recent study](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3561560) suggests that non-pharmaceutical interventions (NPIs) can lead to favorable economic outcomes when appropriately planned. These findings suggest that it's possible to optimize mitigation efforts in a manner that is favorable towards the epidemic and economics. 

In our research, we have found broad discrapency between behaviors in terms of the associated negative economic and psychological even though the difference in epidemic effect may be insignificant. 

### How? 

Pandemik consists of six stand-alone models, each representing a progression from behavior change and mitigation towards the final outcome - a visualized "map" of the relationship different behaviors have with favorable outcomes. Results are presented with sensitivities and confidence intervals. 

stage | name | focus | method 
--- | --- | --- | --- 
1 | country social model | models relevant socio-cultural at a country level | [Hofstede Model](https://www.hofstede-insights.com/product/compare-countries/)
2 | behavioral model | model effects of behaviors | restriction of behavior  | custom differential model
3 | epidemic model (SEIR) | from population to infection | [SEIR](http://www.public.asu.edu/~hnesse/classes/seir.html)
4 | hospitalization model | from infection to hospital | custom differential model
5 | ICU burden model | from hospital to ICU and release or death | [ICUSIM](https://github.com/autonomio/ICUSIM)
6 | output model | summarize results | sensitivity analysis

Each stage accepts inputs, sometimes from one of the preceding steps. Each step gives an output which used by one of the following steps. 

stage | name | input | output
--- | --- | --- | ---
1 | country social model | name of the country | weight
2 | behavioral model | restriction of behavior  | `beta` for SEIR, economic and psychological damage
3 | epidemic model (SEIR) | standard SEIR | number of infectious
4 | hospitalization model | number of infected | number of hospitalized
5 | ICU burden model | number of hospitalized | ICU demand and fatality
6 | output model | various | list of behaviors, economic, psychological, and health outcomes 

<hr>

### Why?

In April 2020, a significant portion of the world's population is adversely affected by pandemic mitigation actions. Public policy is optimized towards public health outcomes, at the expense of economics and psychological effects. Pandemik provides a highly accessible and scientifically robust way to optimize towards economic and psychological outcomes, without compromising public health benefits.

Example use-cases include:

- Plan for policy that optimize balance between public health, economic, and psychological outcomes
- Demonstrate the value of different behaviors and mitigations

<hr>

### How?

Pandemik is dead simple to use. You start by planning your inputs in terms of the behaviors you want to target.

**Inputs:**

- Choose country to model
- Set the degree of restriction (0-100) to one or more +50 relevant behaviors
- Set the time period to simulate (number of days)
- Set the degree of confidence that is acceptable (affects running time / compute requirement) 

**Output:**

- Total economic damage
- Total psychological damage
- Total infected
- Total hospitalized / standard ICU / ventilated
- Total fatalities
- Effect of each behavior (sensitivity to each outcome)
- Recommended behavior plan

<hr>

### 💬 How to get Support

| I want to...                     | Go to...                                                  |
| -------------------------------- | ---------------------------------------------------------- |
| **...troubleshoot**           | [GitHub Issue Tracker]                   |
| **...report a bug**           | [GitHub Issue Tracker]                                     |
| **...suggest a new feature**  | [GitHub Issue Tracker]                                     |
| **...get support**            | [GitHub Issue Tracker]  · [Discord Chat]                         |
| **...have a discussion**      | [Discord Chat]                                            |

<hr>

### 📢 Citations

If you use ICUSIM for published work, please cite:

`Autonomio's Pandemik [Computer software]. (2020). Retrieved from http://github.com/autonomio/pandemik.`

<hr>

### 📃 License

[MIT License](https://github.com/autonomio/pandemik/blob/master/LICENSE)

[github issue tracker]: https://github.com/automio/pandemik/issues

