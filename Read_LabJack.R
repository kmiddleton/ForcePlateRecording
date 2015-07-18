library("ggplot2")
library("reshape2")
library("gridExtra")

infile <- "data_200g.txt"

M <- read.table(infile, skip = 2)

str(M)

freq <- as.numeric(sub("frequency=", "",
                       read.table(infile, as.is = TRUE)[1,1]))

M[, 2] <- M[, 1] - mean(M[1:(freq/2), 1])
M$time <- 1/freq * seq(0, (nrow(M) - 1))

p1 <- ggplot(M, aes(time, V1)) + geom_line()
p2 <- ggplot(M, aes(time, V2)) + geom_line()

grid.arrange(p1, p2)
