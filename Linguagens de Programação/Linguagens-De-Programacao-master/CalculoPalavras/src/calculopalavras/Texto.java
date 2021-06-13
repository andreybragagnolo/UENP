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
import java.util.concurrent.RecursiveTask;

/**
 *
 * @author andre
 */
public class Texto extends RecursiveTask<ArrayList> {

    private ArrayList<Palavras> texto;
    private ArrayList<Palavras> palavras;
    private ArrayList<Palavras> stopwords;
    private  int TamDivision ;

    public int getTamDivision() {
        return TamDivision;
    }

    public void setTamDivision(int TamDivision) {
        this.TamDivision = TamDivision;
    }

    public Texto(ArrayList<Palavras> texto, ArrayList<Palavras> palavras, ArrayList<Palavras> stopwords) {
        this.texto = texto;
        this.palavras = palavras;
        this.stopwords = stopwords;
    }

    public ArrayList<Palavras> recebeTexto(String diretorio) throws FileNotFoundException, IOException {
        String texto;
        texto = "";
        String linha = "";
        FileReader read = new FileReader(diretorio);
        BufferedReader buffer = new BufferedReader(read);
        while ((linha = buffer.readLine()) != null) {
            texto = texto.replace(texto, texto + linha + " ");
        }

        texto = removePontuacao(texto);
        String[] spliter = texto.split(" ");
        ArrayList<Palavras> listPalavras = new ArrayList<>(texto.length());
        for (String item : spliter) {
            Palavras p = new Palavras();
            p.setPalavra(item.toUpperCase());
            listPalavras.add(p);
        }

        return listPalavras;
    }


    public ArrayList<Palavras> getTexto() {
        return texto;
    }

    public void setTexto(ArrayList<Palavras> texto) {
        this.texto = texto;
    }

    public ArrayList<Palavras> getPalavras() {
        return palavras;
    }

    public void setPalavras(ArrayList<Palavras> palavras) {
        this.palavras = palavras;
    }

    public ArrayList<Palavras> getStopwords() {
        return stopwords;
    }

    public void setStopwords(ArrayList<Palavras> stopwords) {
        this.stopwords = stopwords;
    }

    public String removePontuacao(String texto) {
        String semPontuacao = texto.replace('?', ' ');
        semPontuacao = semPontuacao.replace(',', ' ');
        semPontuacao = semPontuacao.replace('.', ' ');
        semPontuacao = semPontuacao.replace('!', ' ');
        semPontuacao = semPontuacao.replace("  ", " ");

        return semPontuacao;
    }

    public ArrayList<Palavras> verificaStopWords(ArrayList texto) throws IOException {
        String diretorioArquivo = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\Stopwords.txt";
        Palavras palavraAuxiliar = new Palavras();
        ArrayList<Palavras> textoAuxiliar = new ArrayList<Palavras>(1000);
        textoAuxiliar = recebeTexto(diretorioArquivo);
        ArrayList<Palavras> listStopWords = new ArrayList<>(textoAuxiliar.size());
        for (Palavras item : textoAuxiliar) {
            Palavras p = new Palavras();
            p.setPalavra(item.getPalavra().toUpperCase());
            listStopWords.add(p);
        }
        return listStopWords;
    }

    public ArrayList<Palavras> verificadorFrequencia(ArrayList<Palavras> texto, int valor, ArrayList<Palavras> stopwords) {
        ArrayList<Palavras> vetorPalavras = new ArrayList<>(valor);
        int quantidade = 0;
        boolean contem = false;
        for (Palavras item : texto) {
            contem = false;
            Palavras auxiliar = new Palavras();
            item.setPalavra(item.getPalavra().toUpperCase());
            auxiliar.setPalavra(item.getPalavra());

            for (Palavras p : vetorPalavras) {
                if (p != null) {
                    if (p.getPalavra().equals(auxiliar.getPalavra())) {
                        contem = true;
                        auxiliar = p;
                    }
                }
            }
            boolean stword = false;
            for (Palavras p : stopwords) {
                if (p != null) {
                    if (p.getPalavra().equals(auxiliar.getPalavra())) {
                        stword = true;
                    }
                }
            }
            if (contem == true && stword == false) {
                quantidade = (auxiliar.getContador() + 1);
                auxiliar.setContador(quantidade);
            } else if (stword == false) {

                auxiliar.setPalavra(item.getPalavra());
                auxiliar.setContador(1);

                vetorPalavras.add(auxiliar);

            } else {

            }
        }
        return vetorPalavras;
    }

    @Override
    protected ArrayList compute() {
        
        if (texto.size() <= TamDivision) {
            return this.verificadorFrequencia(texto, TamDivision, stopwords);
        }
        new ArrayList<Palavras>(texto.subList(0, TamDivision));

        Texto trecho1 = new Texto(new ArrayList<Palavras>(texto.subList(0, TamDivision-1)),palavras, stopwords);
        Texto trecho2 = new Texto(new ArrayList<Palavras>(texto.subList(TamDivision,texto.size())), palavras, stopwords);
        trecho1.fork();
        trecho2.fork();
        ArrayList<Palavras> trecho1Resultado = trecho1.join();
        ArrayList<Palavras> trecho2Resultado = trecho2.join();
        ArrayList<Palavras> listaFinal = new ArrayList<>();
        for (Palavras p : trecho1Resultado) {
            listaFinal.add(p);
        }
        for (Palavras p : trecho2Resultado) {
            listaFinal.add(p);
        }
        return listaFinal;
    }

}


