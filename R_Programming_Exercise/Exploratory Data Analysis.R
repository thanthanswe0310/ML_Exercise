library(tidyverse)

ny <- c(1,2,3,5,6,7,8,9,11,66)

la <- c(1,2,3,4,5,6,7,8,9,10)

pizza <- data_frame(ny,la)

pizza

mean(pizza$ny)
mean(pizza$la)


median(pizza$ny)

x <- table(pizza$ny)
x

names(x)[which(x==max(x))]

summary(pizza)








