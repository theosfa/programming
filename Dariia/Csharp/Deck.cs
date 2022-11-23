using System;

namespace Csharp{

    class Deck{
        
        private int n = 24;
        private Card[] deck = new Card[24];
        private Random rnd = new Random();
    
        public Deck(){
            for (int i = 0; i < this.n; i++){
                this.deck[i] = new Card();
            }
            int num = 10;
            int suit = 1;
            for (int i = 0; i < n; i++){
                    this.deck[i].setNum(num);
                    switch (suit)
                    {
                        case 1:
                            this.deck[i].setSuit("Romb");
                            break;
                        case 2:
                            this.deck[i].setSuit("Diamond");
                            break;
                        case 3:
                            this.deck[i].setSuit("Pick");
                            break;
                        case 4:
                            this.deck[i].setSuit("Treph");
                            break;
                    }
                    
                    num++;
                    if (num == 16){
                        num = 10;
                        suit++;
                    }
            }
        }

        public Card[] getDeck(){
            return this.deck;
        }

        public int getN(){
            return this.n;
        }

        public Card getRandomCard(){
            int rand1 = this.rnd.Next(this.n);
            Card card = this.deck[rand1];
            this.deck[rand1] = this.deck[this.n-1];
            this.n--;
            return card;
        }

    }
}