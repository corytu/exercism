# This is a stub function to take two strings
# and calculate the hamming distance
hamming <- function(strand1, strand2) {
  nucleotides_list <- strsplit(c(strand1, strand2), "")
  if (length(unique(sapply(nucleotides_list, length))) > 1) {
    stop("Strand 1 and strand 2 have unequal lengths")
  }
  sum(nucleotides_list[[1]] != nucleotides_list[[2]])
}
