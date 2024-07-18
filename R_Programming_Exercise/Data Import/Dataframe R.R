# Data import into R


library(tidyverse)
starwars

my.wars <- as.data.frame(starwars)

my.wars <- my.wars[,-(11:13)]

my.wars

head(my.wars)
tail(my.wars)


mark <- c(37.5,34.75,34.25,0,0,0.75,0)
carrie <- c(13.5,22.75,21.25,0,0,0.5,5.75)

my.data$MarkScreenTime <-mark
my.data$CarrieScreenTime <- Carrie
my.data


