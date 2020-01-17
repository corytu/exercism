number_type <- function(n) {
  if ((n %% 1) != 0 | n <= 0) {
    stop("n should be a natual number")
  }
  # Use integer to speed up finding factors
  # https://stackoverflow.com/a/6425726/6666231
  n <- as.integer(n)
  if (n == 1L) {
    return("deficient")
  }
  n_seq <- 1:(n - 1)
  n_factors <- n_seq[(n %% n_seq) == 0L]
  aliquot_sum <- sum(n_factors)
  if (aliquot_sum == n) {
    return("perfect")
  } else if (aliquot_sum > n) {
    return("abundant")
  } else {
    return("deficient")
  }
}
