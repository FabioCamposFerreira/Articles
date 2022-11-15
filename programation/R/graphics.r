# -------------------------
# Histogram  
numbers = c(seq(1:9))
hist(numbers)

# -------------------------
# Dispersion
numbers = c(seq(1:9))
plot(numbers)

# -------------------------
# Dispersion
numbers = c(seq(1:9))
plot(numbers)

# -------------------------
# ??
numbers = c(seq(1:9))
install.packges("ggplot2")
library(ggplot2)
ggplot(numbers, aes(am))+geom_bar()

# ---------------------------------------------
# Boxplot
summary and boxplot