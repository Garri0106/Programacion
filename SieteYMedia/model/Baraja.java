package SieteYMedia.model;

import java.util.Random;

public class Baraja {
	private Carta[] cartas;
	private final static int MAX_SIZE = 40;
	private int siguiente;
	
	public Baraja() {
		this.cartas = new Carta[MAX_SIZE];
		this.siguiente = 0;
		int posicion = 0;
		for (Palo palo : Palo.values()) {
			for (int i = 0; i<13; i++) {
				if (i != 8 && i != 9) {
					try {
						this.cartas [posicion] = new Carta (i, palo);
						posicion++;
					} catch (Exception e) {
					}
				}
			}
		}
	}
	public Carta getSiguiente() {
		return this.cartas[siguiente++%MAX_SIZE];
	}
		
	public void barajar() {
		Random random = new Random();
		Carta aux;
		for (int i = 0; i<MAX_SIZE; i++) {
			int randomNum = random.nextInt((MAX_SIZE - 0) + 1) + 0;
			aux = cartas[i];
			cartas[i] = cartas[randomNum%MAX_SIZE];
			cartas[randomNum%MAX_SIZE] = aux;
			
		}
	}
}
