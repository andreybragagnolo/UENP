/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculopalavras;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.RecursiveTask;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author andre
 */
public class Palavras {

    private String palavra;
    private int contador;


    public Palavras() {

        palavra = "";
        contador = 0;

    }

    public Palavras(String palavra, int contador) {
        this.palavra = palavra;
        this.contador = contador;

    }

    public int getContador() {
        return contador;
    }

    public void setContador(int contador) {
        this.contador = contador;
    }

    public String getPalavra() {
        return palavra;
    }

    public void setPalavra(String palavra) {
        this.palavra = palavra;
    }
    public int compareTo(Palavras p) {
        return this.getPalavra().compareTo(p.getPalavra());
    }
    



}
