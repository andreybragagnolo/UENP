/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paralelismo;

import java.time.Duration;
import java.time.Instant;

/**
 *
 * @author andre
 */
public class Paralelismo {

    public static void main(String[] args) {
        EncontrarVogais ev = new EncontrarVogais("");
        ev.setTexto(ev.geradorDeTexto());
        Instant Start = Instant.now();
        System.out.println("Contador =" + ev.compute());
        Instant End = Instant.now();
        Duration total = Duration.between(Start, End);
        long totalms = total.toMillis();
        System.out.println("Duração Tarefa Paralela =" + totalms+"ms");
        Start = Instant.now();
        int vogTotal = ev.calcularVogais(ev.getTexto());
        End = Instant.now();
        total = Duration.between(Start, End);
        totalms = total.toMillis();
        System.out.println("Duração Tarefa Não Paralela ="+totalms+"ms");
    }

}
