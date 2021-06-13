/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paralelismo;

/**
 *
 * @author andre
 */
public class Threads extends Thread {

    @Override
    public void run() {
       
    }

    public static void insertionSort(int[] vetor) {
        int j;
        int valorComparado;
        int i;

        for (j = 1; j < vetor.length; j++) {
            valorComparado = vetor[j];
            for (i = j - 1; (i >= 0) && (vetor[i] > valorComparado); i--) {
                vetor[i + 1] = vetor[i];
            }
            vetor[i + 1] = valorComparado;
        }
    }
}
