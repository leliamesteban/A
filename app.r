# jessesadler.com/post/geocoding-with-r
library(ggplot2)
library(maptools)
library(maps)

visited <- c("Spain", "France")
locations <- geocode(visited)
place.x <- locations.visited$lon
place.y <- locations.visited$lat

map("world", fill=TRUE, col="white", bg="lightblue", ylim=c(-60, 90), mar=c(0,0,0,0))
points(place.x, place.y, col="red", pch=16)
