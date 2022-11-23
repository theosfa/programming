using System;

namespace Csharp{

    class Card{
        
        private int num = 0;
        private string suit = "";

        public Card(){
        }

        public void setNum(int num){
            this.num = num;
        }

        public void setSuit(string suit){
            this.suit = suit;
        }

        public int getNum(){
            return this.num;
        }
        public string getSuit(){
            return this.suit;
        }
    }
}