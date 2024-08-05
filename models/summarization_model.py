from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    text = "The cat is sitting on the mat. It looks very happy and comfortable."
    summary = summarize_text(text)
    print(summary)
