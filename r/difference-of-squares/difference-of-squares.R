# this is a stub function that takes a natural_number
# and should return the difference-of-squares as described
# in the README.md
difference_of_squares <- function(natural_number) {
  natural_numbers <- 1:natural_number
  return(sum(natural_numbers)^2 - sum(natural_numbers^2))
}
