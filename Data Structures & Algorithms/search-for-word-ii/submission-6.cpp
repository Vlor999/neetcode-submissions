#include <vector>
#include <string>
#include <set>
#include <tuple>

using namespace std;

class Solution {
    public:
        string convListToString(vector<int> position) {
            return to_string(position[0]) + "/" + to_string(position[1]);
        }

        vector<vector<int>> foundStartPosition(vector<vector<char>>& board, char lettre) {
            vector<vector<int>> pointDepart;
            int nombreLigne = board.size();
            int nombreColonne = board[0].size();
            for (int l = 0; l < nombreLigne; l++) {
                for (int c = 0; c < nombreColonne; c++) {
                    if (board[l][c] == lettre) {
                        pointDepart.push_back({l, c});
                    }
                }
            }
            return pointDepart;
        }

        vector<vector<int>> positionAutour(int nombreLigne, int nombreColonne, vector<int> position, const set<string>& alreadySeen) {
            int l = position[0];
            int c = position[1];
            
            vector<vector<int>> output;
            vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            
            for (const vector<int>& dir : directions) {
                int futurL = l + dir[0];
                int futurC = c + dir[1];
                vector<int> futurPos = {futurL, futurC};
                string newPosStr = convListToString(futurPos);
                if (0 <= futurL && futurL < nombreLigne && 0 <= futurC && futurC < nombreColonne && alreadySeen.find(newPosStr) == alreadySeen.end()) {
                    output.push_back(futurPos);
                }
            }
            return output;
        }

        bool findWord(vector<vector<char>>& board, string word) {
            int nombreLigne = board.size();
            int nombreColonne = board[0].size();
            vector<vector<int>> startPosition = foundStartPosition(board, word[0]);
            
            if (startPosition.empty()) {
                return false;
            }
            
            for (const vector<int>& debut : startPosition) {
                vector<tuple<int, set<string>, vector<int>>> toSee = {{0, {convListToString(debut)}, debut}};
                
                while (!toSee.empty()) {
                    auto [posLettre, alreadySeenCurrent, possiblePosition] = toSee.back();
                    toSee.pop_back();
                    
                    if (posLettre == word.size() - 1) {
                        return true;
                    }
                    
                    char nextChar = word[posLettre + 1];
                    for (const vector<int>& nextPos : positionAutour(nombreLigne, nombreColonne, possiblePosition, alreadySeenCurrent)) {
                        if (board[nextPos[0]][nextPos[1]] == nextChar) {
                            set<string> newSeen = alreadySeenCurrent;
                            newSeen.insert(convListToString(nextPos));
                            toSee.push_back({posLettre + 1, newSeen, nextPos});
                        }
                    }
                }
            }
            return false;
        }

        vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
            vector<string> output;
            if (board.size() == 0){
                return output;
            }
            for (const string& word : words) {
                if (findWord(board, word)) {
                    output.push_back(word);
                }
            }
            return output;
        }
};
