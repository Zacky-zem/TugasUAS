import pandas as pd
from sentiment_model import analyze_sentiment

def process_data(file_path):
    # Membaca data
    data = pd.read_csv(file_path)
    
    # Menambahkan kolom hasil analisis
    data['predicted_polarity'] = data['text'].apply(analyze_sentiment)
    
    # Menampilkan hasil
    print("Hasil Analisis Sentimen:")
    print(data)
    return data

if __name__ == "__main__":
    process_data("app/data.csv")
