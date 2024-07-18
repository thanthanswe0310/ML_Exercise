# Linear Regression Exercise in R
library(psych)
library(ggplot2)

college <- read.csv("C:/Users/thanthanswe/Documents/R/365DataScience_R/regression-example.csv")

college

describe(college)

linmod <- lm(GPA ~ SAT,data = college)

ggplot(college,aes(SAT,GPA))+ geom_point()+theme_light()+
  labs(x="SAT Scores",y="GPA upon graduation", title="SAT and GPA")+
  stat_smooth(method="lm",se=FALSE)

summary(linmod)