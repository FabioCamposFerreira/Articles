# ---------------------------------
# Vectores
numbers <- c(1,2,3,4,5,6,7,8,9)
print(numbers)
# ??

names <- c("John", "Marta", "Julia", "Cleiton")
print(names)
# ?? 

# Acess element
print(numbers[1])
# ??

# Acess range
print(names[1:3])
# ??
# Remove item
numbers[-9]
print(numbers)
# ??

# Change item 
name(2) <- "Edu"
print(names)
# ??

# Add new element
numbers[10] <- 10

# Clear vector
names <- NULL

# ------------------------------------------------------------
# Factor
Countries <- factor (c("US", "Brazil", "French", "Spain", "United Kingdom"))
print (Countries)
# ??
# ??

# Order factors
olympics.medals <- factor(c("prate", "our","bronze"), 
                            levels = c("bronze","prate", "our"),
                            ordered = TRUE)
print(olympics.medals)                            
# ??
# ??                         

# ----------------------------------------------------------------
# List
people <- list(sex = "M", city="London", age = 21)
print(people)
# ??
# ??
# ??

# Acess item 
print(people[1])
# ?? 

# Acess value
print(people[[1]])
# ??
# Change value
people[["age"]] <- 33
print (people)
# ??

# Revome element
people[["city"]] <- NULL
print (people)
# ??

# Filter
animal <- list(specie="dog", patas="4", asas="0")
print(animal[c("specie", "asas")])
# ??

# List of vectors 
temperature = c(20,24,30)
city = c("New York","Tokyo","Paris")
population = c(10000,15000,20000)
citys <- list(city=city,temperature=temperature,population=population)
print(citys)
# ??

# Mean of the elements
numbers = list(seq(1:9), seq(10:19))
print(lapply(numbers, mean))
# ??
print(sapply(numbers, mean))
# ??

# ------------------------------------------------------------------------
# Data Frame

# from vectors
temperature = c(20,24,30)
city = c("New York","Tokyo","Paris")
df1 <- data.frame(city,temperature)
print(df1)
# ??

# from list
temperature = c(20,24,30)
city = c("New York","Tokyo","Paris")
population = c(10000,15000,20000)
citys <- list(city=city,temperature=temperature,population=population)
df2 <- data.frame(city,temperature)
print(df2)
# ??

# Acess element 
print(df2[1,2]) 
# ??

# Acess column
print(df2[,2])
# ??
print(df2["temperature"])
# ??
print(select(df2,1:2))
# ??


# Acess row
print(df2[,2])
# ??
print(slice(df2,1:2))
# ??

# Acess interval
print(df2[c(1:3),c(1,3)])
# ??

# Extract columns names
print(names(df2))
# ??

# Get dimension of the data frame
print(dim(df2))
# ??

# Get details of the data frame
print (str(df2))
# ??
library(DPLYR)
print (glimpse(df2))
# ??


# Join
df1 <- data.frame(People=c(1,2,3,4), hight=c(173,181,177,189))
df2 <- data.frame(People=c(1,2,3,4), weight=c(70,80,120,91))
df3 <- inner_join(df1,df2,"People")
print(df3)
# ??

# Filter
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04))
dogs <-  filter(df1, Animal=="Dog")
print(dogs)
# ??f

# Delete column
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04),, size=c(0.15,0.46,1.00,0.04))
print(select(df1, -weight))
# ??

# Add new column
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04),, size=c(0.15,0.46,1.00,0.04))
df2 <- mutate(df1, color=c("Black", "Yellow", "Brow and white", "Green"))
print(df2)
# ??

# Order
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04),, size=c(0.15,0.46,1.00,0.04))
print(select(df1,weight) %>% arrange(weight))
# ??

# Group elements by column
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04),, size=c(0.15,0.46,1.00,0.04))
print(df1 %>% group_by(Animal) %>% sumarise(mean(weight)))
# ??

# Transform rows to columns
library(tidyr)
df1 <- data.frame(Animal=c("Dog","Cat","Dog","Bird"), weight=c(25,3,40,0.04), size=c(0.15,0.46,1.00,0.04))
df2 <- separate(df1, "Animal","Weight")

# Separate text in column
library(dplyr)
df1 <- data.frame(date=c("2022.01",'2022.03',"2022.05","2022.09"), sellers=c(12000,1000,13000,9000))
df1 <- separete(df1, date, "year", "mouth")
df1 <- df1[-1]
print(df1)
# ??

# United columns
??

# Save
write.csv()

# ---------------------------------------------
# Matriz
m <- matrix (seq(1:9), nrow = 3)
print(m)
# ??
m2 <- matrix (seq(1:25), ncol = 5, byrow = TRUE, dimnames = list(c(seq(1:5)), c("A", "B", "C", "D", "E")))
print(m2)
# ??

# Acess elements
print(m2[c(1:2), c("B","C")])
# ??

# Sum row
print(apply(m2,1, sum))
# ??

# Sum columns
print(apply(m2,2, sum))
# ??