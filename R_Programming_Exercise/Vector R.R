age <- c(23,26,24,26)

attributes(age)

names(age)

names(age)<- c("George","John","Paul","Ringo")
age

attributes(age)

names(age)


names(age)<- c("George Harrison","John Lennon","Paul McCartney","Ringo Starr")

age

names(age)<-NULL
age


n.deck <- c(6,6,7,8,9,10)
deck<- c("Duke","Assasin","Captain","Ambassaror","Contessa")

deck[4]

deck[-4]

deck[c(1,3,5)]


n.deck["Contessa"]

