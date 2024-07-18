marital.status <- c("Married","Married","Single","Married","Divorced","Widowed",
                    "Divorced")

str(marital.status)

marital.factor <- factor(marital.status)

marital.factor

typeof(marital.factor)
str(marital.factor)

new.factor <- factor(marital.status,
                     levels = c("Single","Married","Divorced","Widowed"))

str(new.factor)

levles(new.factor)<- c("s","m","d","w")

str(new.factor)

new.factor<- factor(marital.status,
                    levles = c("Single","Married","Divorced","Widowed")
                    )
str(new.factor)



