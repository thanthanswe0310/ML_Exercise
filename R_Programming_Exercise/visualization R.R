df$Survived <- as.factor(df$Survived)
df$Pclass   <- as.factor(df$Pclass)
df$Sex      <- as.factor(df$Sex)
df$Embarked <- as.factor(df$Embarked)

df

hist <- ggplot(data= df,aes(x=Age),

hist+geom_histogram(binwidth =5, color="darkslategray",
                                   fill ="darkslategray4",alpha =0.5)+
              ggtitle("Age Distribution on the Titanic")+
                labs(y="Number of passangers ",x="Age")+
                 theme_minimal()
                                   )
               

