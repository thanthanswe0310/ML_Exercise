my.book <- list(Name = "1984",Author= "George Orwell",Published="1944",
                Contents = list(PartOne= c(1:18),
                                PartTwo= c(1:10),
                                PartThree = c(1:6),
                                Appendix = "Nrespeak"))
               

my.book

str(my.book)

new.book <- list("1984","George Orwell",1949,
                 list(c(1:8),c(1:10),c(1:6),"Newspeak"))

names(new.book)<- c("Name","Author","Published","Contents")

str(new.book)

