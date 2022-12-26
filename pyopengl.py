import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

# import gflw
# import pyopengl
# use numpy


def main():


    if not glfw.init():
        return


    window = glfw.create_window(720, 600, "Pyopengl Coloring Triangle", None, None)

    if not window:
        glfw.terminate()
        return


    glfw.make_context_current(window)

                #Postions       #Colors
    triangle = [-0.5,-0.5,0.0, 3.5,0.0,0.0,
                 0.5,-0.5,0.0, 0.0, 3.5, 0.0,
                 0.0,0.5,0.0 ,  0.0,0.0,3.5]


    triangle = np.array(triangle, dtype = np.float32)



    VERTEX_SHADER = """

        #version 330

        in vec3 position;
        in vec3 color;
        out vec3 newColor;
        
        void main() {
         
         gl_Position = vec4(position, 1.0);
         newColor = color;
     
          }


    """

    FRAGMENT_SHADER = """
        #version 330
        
        in vec3 newColor;
        out vec4 outColor;

        void main() {

          outColor = vec4(newColor, 1.0f);

        }

    """

    # Compila o Programa e os shaders

    shader =  OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(VERTEX_SHADER,GL_VERTEX_SHADER),
                                             OpenGL.GL.shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER))


    # Cria um buffer do objeto na gpu
    VBO = glGenBuffers(1)

    # Liga o Buffer para ajudar no processamento
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)



    # Pega a posição do shader
    position = glGetAttribLocation(shader, 'position')
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    # Pega a cor do Shader
    color = glGetAttribLocation(shader, 'color')
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    glUseProgram(shader)






    glClearColor(0.0,0.0,1.0,1.0)




    # Desenha o Triangulo
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        

        glDrawArrays(GL_TRIANGLES, 0, 3)


        glfw.swap_buffers(window)


    glfw.terminate()





#Metodo para manter a janela aberta

if __name__ == "__main__":
    main()