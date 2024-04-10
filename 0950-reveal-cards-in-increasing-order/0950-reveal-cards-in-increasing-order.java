class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        int l = deck.length;
        int[] res = new int[l];
        ArrayList<Integer> ind = new ArrayList<>();
        
        for (int x=0; x<l; x++){
            ind.add(x);
        }
        
        for (int i=0; i<l; i++){
            if (i == l-1) break;
            else {
                int k = ind.remove(i+1);
                ind.add(k);
            }
        }
        
        for (int j=0; j<ind.size(); j++){
            int val = ind.get(j);
            res[val] = deck[j];
        }
        
        return res;
    }
}