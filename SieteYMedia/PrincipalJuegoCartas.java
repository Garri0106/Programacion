package SieteYMedia;

import java.util.Scanner;
import java.lang.Thread;

import SieteYMedia.model.Baraja;
import SieteYMedia.model.Carta;

public class PrincipalJuegoCartas {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String eleccion;
		Baraja baraja_portuguesa = new Baraja();
		baraja_portuguesa.barajar();
		Carta cartasUsuario [] = new Carta[10];
		Carta cartasBanca [] = new Carta[10];
		Integer contador = 0;
		double valorUsuario = 0;
		Double valorBanca = 0.0;
		int haPasado = 0;
		int contadorBanca = 0;
		do {	//El usuario obtiene cartas
			cartasUsuario[contador] = baraja_portuguesa.getSiguiente();
			valorUsuario += cartasUsuario[contador].getValor();
			System.out.println("Sua carta é: "+cartasUsuario[contador]);
			System.out.println("O valor das suas cartas é: "+valorUsuario);
			if (valorUsuario > 7.5) {
				break;
			}
			System.out.println("Quer pegar outra carta? (Sim / Não): ");
			eleccion = scanner.nextLine();
			if (!eleccion.toLowerCase().equals("sim") && !eleccion.equalsIgnoreCase("nao")) {
				System.err.println("Escolha errada.");
				System.out.println("Quer pegar outra carta? (Sim / Não): ");
				eleccion = scanner.nextLine();
				contador++;
			}
		}while (eleccion.toLowerCase().equals("sim"));
		if (haPasado == 0) {
			//La banca coge valores
			do{   
				cartasBanca[contadorBanca++] = baraja_portuguesa.getSiguiente();
				valorBanca+=cartasBanca[contadorBanca-1].getValor();
				System.out.println("O banco tira um "+cartasBanca[contadorBanca-1]+
			     " Valor presente do banco = "+valorBanca);
			   try {
			    Thread.sleep(2000);
			   }catch(InterruptedException e) {
				   
			   }
			   }while (valorBanca<valorUsuario && valorBanca<7.5 && valorUsuario<=7.5);
			//Termina los valores de la banca
			System.out.println("O banco tem um valor de: "+valorBanca);
			//Se comparan los valores de ambos (banca y usuario)
			if (valorUsuario > 7.5 || ((valorBanca > valorUsuario) && valorBanca <= 7.5)) {
				System.out.print("Perdeste, ");
				System.err.println("inutil.");
				}
				else if (valorUsuario > valorBanca || valorBanca > 7.5) {
					System.out.println("Parabéns! Você ganhou.");
				}
				else {
					System.out.println("Bem, você acabou de empatar com o banco campeão.");
				}
		}
	}
}
