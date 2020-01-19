parse_phone_number <- function(number_string) {
  cleansed_number_string <- gsub("[\\.()+[:blank:]-]", "", number_string)
  # "Real values larger in modulus than the largest integer are coerced to NA"
  if (is.na(as.numeric(cleansed_number_string))) {
    return(NULL)
  }
  if (nchar(cleansed_number_string) < 10 | nchar(cleansed_number_string) > 11 | (nchar(cleansed_number_string) == 11 & !grepl("^1", cleansed_number_string))) {
    return(NULL)
  } else if (nchar(cleansed_number_string) == 11 & grepl("^1", cleansed_number_string)) {
    cleansed_number_string <- gsub("^1", "", cleansed_number_string)
  }
  numbers <- sapply(unlist(strsplit(cleansed_number_string, "")), as.integer, USE.NAMES = FALSE)
  if (numbers[1] < 2 | numbers[4] < 2) {
    return(NULL)
  } else {
    return(cleansed_number_string)
  }
}
