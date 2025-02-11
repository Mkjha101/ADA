#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

// Common words to ignore
set<string> common_words = {"is", "am", "are", "was", "were", "be", "been", "being",
                            "have", "has", "had", "having", "do", "does", "did",
                            "a", "an", "the", "and", "of", "on", "in", "to", "with", 
                            "for", "it", "at", "i"};

vector<string> create_vector_from_file(const string& filename) {
    vector<string> words;
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Could not open the file: " << filename << endl;
        exit(EXIT_FAILURE);
    }

    string word;
    while (file >> word) {
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        word.erase(remove_if(word.begin(), word.end(), ::ispunct), word.end());

        if (!word.empty() && common_words.find(word) == common_words.end()) {
            words.push_back(word);
        }
    }

    file.close();
    return words;
}

vector<int> create_word_frequency_vector(const vector<string>& words, const set<string>& uniqueWords) {
    vector<int> wordFreq(uniqueWords.size(), 0);
    size_t index = 0;

    for (const string& word : uniqueWords) {
        wordFreq[index] = count(words.begin(), words.end(), word);
        index++;
    }
    
    return wordFreq;
}

double cosine_similarity(const vector<int>& vec1, const vector<int>& vec2) {
    double dotProd = 0.0, magVec1 = 0.0, magVec2 = 0.0;

    for (size_t i = 0; i < vec1.size(); ++i) {
        dotProd += vec1[i] * vec2[i];
        magVec1 += vec1[i] * vec1[i];
        magVec2 += vec2[i] * vec2[i];
    }

    if (magVec1 == 0.0 || magVec2 == 0.0) { // Avoid division by zero 
        return 0.0;  
    }

    return dotProd / (sqrt(magVec1) * sqrt(magVec2));
}

int main() {
    string file1 = "input1.txt";
    string file2 = "input2.txt";

    vector<string> words1 = create_vector_from_file(file1);
    vector<string> words2 = create_vector_from_file(file2);

    set<string> uniqueWords(words1.begin(), words1.end());
    uniqueWords.insert(words2.begin(), words2.end());

    vector<int> freqVector1 = create_word_frequency_vector(words1, uniqueWords);
    vector<int> freqVector2 = create_word_frequency_vector(words2, uniqueWords);

    cout << "Words in File1: ";
    for (const string& word : words1) cout << word << " ";
    cout << endl;

    cout << "Words in File2: ";
    for (const string& word : words2) cout << word << " ";
    cout << endl;

    cout << "Frequency Vector 1: ";
    for (int val : freqVector1) cout << val << " ";
    cout << endl;

    cout << "Frequency Vector 2: ";
    for (int val : freqVector2) cout << val << " ";
    cout << endl;

    double similarity = cosine_similarity(freqVector1, freqVector2);
    cout << "Cosine Similarity between the vectors: " << similarity << endl;

    return 0;
}