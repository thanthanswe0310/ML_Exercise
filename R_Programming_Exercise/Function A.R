

## ------------- Building A Function -------------------#

deck <- c("Duke","Assassin","Captain","Ambassador","Contessa")
#print(deck)


sample(deck,size = 3)


draw <- function(){
  deck <- c("Duke","Assassin","Captain","Ambassador","Contessa")
  hand <- sample(deck,size=3, replace=T)
  print(hand)
}

draw()