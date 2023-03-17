package Enumerados.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

import Enumerados.Desplazable;

public class Persona implements Desplazable, Comparable<Persona> {
	private String nombre;
	private String apellidos;
	private Genero genero;
	private LocalDate fechaNacimiento;
	
	
	public Persona(String nombre, String apellidos, Genero genero, LocalDate fechaNacimiento) {
		super();
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.genero = genero;
		this.fechaNacimiento = fechaNacimiento;
	}

	public int getEdad() {
		return (int) (ChronoUnit.YEARS.between(fechaNacimiento, LocalDateTime.now()));
	}

	public int compareTo(Persona o) {
		return this.genero.compareTo(o.genero);
	}

	@Override
	public String toString() {
		return "Soy " + genero + " y me llamo " + nombre + " " + apellidos + " y tengo "+ getEdad() + " años";
	}

	@Override
	public void agacharse() {
		System.out.println("Agachado.");
	}

	@Override
	public void moverse() {
		System.out.println("Moviendose...");
	}

	@Override
	public void correr() {
		System.out.println("Corriendo...");
	}

	@Override
	public void saltar() {
		System.out.println("*salta*");
	}
	
}
