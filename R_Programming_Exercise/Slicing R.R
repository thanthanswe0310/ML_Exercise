
hp.mat <- matrix(gross, nrow=8,byrow=T)

hp.mat[6,2]
hp.mat[6]
hp.mat[6,]
hp.mat[,2]

hp.snip <- hp.mat[c(1,3,7),]

hp.snip

colnames(hp.mat)<- c("USA","Worldwide")
rownames(hp.mat)<- c("Hallow Part 2","Sorcerer's Stone","Hallows Part 1","Order",
                     "Prince","Golet","Chamber","Prisoner")

hp.mat

hp.mat["Globlet",]
hp.mat[,"USA"]