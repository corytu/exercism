# This is a stub function to take two strings
# and calculate the hamming distance
hamming <- function(strand1, strand2) {
  if (nchar(strand1) != nchar(strand2)) {
    stop("Strand 1 and strand 2 have unequal lengths")
  }
  nucleotides_list <- strsplit(c(strand1, strand2), "")
  sum(nucleotides_list[[1]] != nucleotides_list[[2]])
}
