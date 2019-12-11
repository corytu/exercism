raindrops <- function(number) {
  sounds <- list("Pling", "Plang", "Plong")
  mask <- c(number %% 3 == 0, number %% 5 == 0, number %% 7 == 0)
  ifelse(any(mask), do.call(paste0, sounds[mask]), as.character(number))
}
