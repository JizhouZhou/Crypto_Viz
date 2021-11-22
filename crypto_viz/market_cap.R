library(gdata)
library(ggplot2)

files <- list.files(path = paste(getwd(), '/data', sep = ''))

cap_df <- read.csv(paste('data/', files[1], sep = ''))
cap_df <- data.frame(cap_df$Date, cap_df$Cap)
cap_df$Date <- as.Date(temp$temp.Date, format = '%b %d, %Y')
cap_df <- data.frame(cap_df$Date, cap_df$cap_df.Cap)

i <- 2

temp <- read.csv(paste('data/', files[i], sep = ''))
temp <- data.frame(temp$Date, temp$Cap)
temp$Date <- as.Date(temp$temp.Date, format = '%b %d, %Y')
temp <- data.frame(temp$temp.temp.Date, temp$temp.Cap)

for (i in 2:length(files)) {
  temp <- read.csv(paste('data/', files[i], sep = ''))
  temp <- data.frame(temp$Date, temp$Cap)
  temp$Date <- as.Date(temp$temp.Date, format = '%b %d, %Y')
  temp <- data.frame(temp$temp.Date, temp$temp.Cap)
  mv(from = 'temp', to = gsub(".csv", "", files[i]))
}

