package org.njsoly.tinker

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.core.main
import com.github.ajalt.clikt.parameters.arguments.argument
import com.github.ajalt.clikt.parameters.arguments.default
import com.github.ajalt.clikt.parameters.types.int

class EchoALoop : CliktCommand() {
    val count by argument().int().default(3)

    override fun run() {
        repeat(count) { i ->
            echo("A $i")
        }

    }
}

fun main(args: Array<String>) {
    println("Hello, this is Clikt tinker main.")

    EchoALoop().main(args)
}
