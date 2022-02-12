#The implementation was coded in R

#import libraies
library(pdftools)
library(tmcn)
library(stringr)
library(jiebaR)
library(chinese.misc) #if the PDF is in Chinese version
library(wordcloud)
library(corpus)
library(tm)

files <- list.files(pattern = "pdf$")
length(files)

#combine all files into a single file
pdf_combine(files[1:300], output = "joined-1.pdf")
pdf_combine(files[301:600], output = "joined-2.pdf")
pdf_combine(files[601:900], output = "joined-3.pdf")
pdf_combine(files[901:1162], output = "joined-4.pdf") #the script might collapse when dealing with too many files in one combine
#it is much safer to simply combine them seperately
...
pdf_combine(c("joined-1.pdf", "joined-2.pdf", "joined-3.pdf", "joined-4.pdf"), output = "final-joined.pdf")

#extract texts from the combined PDF file
pdf.text <- pdftools::pdf_text("final-joined.pdf")
texts <- paste(pdf.text)

View(texts)

#segment the texts
cutter <- worker()
segWords <- segment(texts, cutter)
segWords

#remove numbers from the texts
no_number <- gsub("[0-9a-zA-Z/.]+?", "", segWords)  #regular expression
no_number

#define stopwords in a .txt file and remove
new_cutter <- worker(type = "tag", stop_word="stop_words.txt")
pos <- segment(no_number, new_cutter)
pos

length(pos)

#define the texts length
res = list()
for (i in 1:461253) {  #this can be adjusted based on the length of 'pos'
  tryCatch(
    expr = {
      if (pos[i][(tag="n")] != 'NA') {
        res <- append(res, pos[i])
      }
    },
    error = function(e){ 
    }
  )
}

res
res1 <- as.character(res)

#define the number of final texts with frequency
keys <- worker("keywords",topn=100)

final <- vector_keywords(res1, keys)
final

#visualization of the extracted rules

library(plyr) 

tableWord <- count(res1)
View(tableWord)

library(wordcloud) 
windowsFonts(myFont = windowsFont("楷体")) ## Use Chinese color cloud font if they are in Chinese

wordcloud(tableWord[,1], tableWord[,2], 
          random.order = F, col = (length(freq)), min.freq=10, family = "myFont")
