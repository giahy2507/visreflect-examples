# Load necessary library
library(ggplot2)

# Data
weeks <- c('0-4 weeks', '5-8 weeks', '9-12 weeks', '13-16 weeks', '17-20 weeks', '21-26 weeks')
episodes <- c(194, 65, 44, 31, 24, 7)
data <- data.frame(weeks, episodes)

# Plot
ggplot(data, aes(x = weeks, y = episodes)) +
  geom_bar(stat = 'identity', fill = 'lightblue') +
  geom_text(aes(label = paste('n=', episodes, sep='')), vjust = -0.5) +
  labs(x = 'Weeks', y = 'Number of episodes mastitis / women breastfeeding - weeks * 1000',
       title = 'Number of episodes mastitis / women breastfeeding over different weeks') +
  theme_minimal()