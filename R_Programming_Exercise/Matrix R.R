
mtrx <- matrix(1:12,nrow=3)
mtrx

mtrx <- matrix(1:12,ncol=4)
mtrx

mtrx <- matrix(1:12,ncol=4,byrow=TRUE)
mtrx

usa <- c(1.3,1.5,1.2,1.4,1.5)
usa

de <- c(0.2,0.4,0.7,0.8,0.8)
de

ngo <- cbind(usa,de)
ngo

rownames(ngo) <- c("2013","2014","2015","2016","2017")
ngo

ngo <- t(ngo)
ngo


ind <- c(2,2.2,2.4,2.5,2.6)
ngo <- rbind(ngo,ind)
ngo



gdp <- matrix(c(47.9,41.2,41.9,54.6,57.6,1.6,1.6,1.7),
              nrow=3,byrow=TRUE,
              dimnames = list(c("de","usa","ind"),
                              c("2014","2015","2016")
                              )
              )

gdp

exmpl <- matrix(1:10,nrow=4,ncol=4)
exmpl


gross <- c(381,1340,318,975,396,960,292,
           940,302,934,290,897,262,879,249,979
           )

hp.mat <- matrix(gross, nrow=8,byrow=T)

hp.mat


hp.mat[6,2]

hp.mat[6]


hp.mat[,2]


hp.mat[6,]


b.office <- c(171.5,292,281.6,460.6,139.3,288)

matrix.mat <- matrix(b.office,nrow=3,byrow=T,
                     dimnames = list(c("The Matrix","Reloaded","Revolutions"),
                                     c("US","Worldwide")
                                     ))
matrix.mat

matrix.scaled <- matrix.mat/1000

matrix.scaled

avg.margin <- matrix.mat -121

avg.margin

budget <- matrix(c(63,150,150),nrow=3,ncol=2)

budget

margin <- matrix.mat - budget

margin

# matrix multiplication

colMeans(matrix.mat)


colSums(matrix.mat)

total <- colSums(matrix.mat)
rowSums(matrix.mat)

average <- colMeans(matrix.mat)
rowMeans(matrix.mat)



matrix.prelim <- rbind(matrix.mat,average,total)
matrix.prelim

