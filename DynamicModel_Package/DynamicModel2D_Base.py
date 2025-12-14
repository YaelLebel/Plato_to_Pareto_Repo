from DynamicModel_Package.ModelBase import DynamicModel
import matplotlib.pyplot as plt
import numpy as np

class DynamicModel2D (DynamicModel):
    def __init__ (self,variable_x,derivative_function_x,parameters_x,
                  variable_y,derivative_function_y,parameters_y):
        DynamicModel.__init__(self)
        self.add_variable(variable_x,derivative_function_x,parameters_x,'x')
        self.add_variable(variable_y,derivative_function_y,parameters_y,'y')
        self.variable_x = variable_x
        self.variable_y = variable_y
        self.nullclines = {}
    
    def add_variable(self, name, derivative_function, parameters,axis):
        """
        Add a variable to the model with its time derivative function and parameters.
        
        Parameters:
            name (str): Name of the variable.
            derivative_function (function): Function describing the time derivative of the variable.
            parameters (dict): Parameters required by the derivative function.
        """
        self.variables[name] = {
            'derivative_function': derivative_function,
            'parameters': parameters,
            'axis':axis
        }
    
    def add_nullcline(self, name, nullcline_function, parameters,y_fun_x):
        """
        Add a nullcline of a variable to the model with its function and parameters.
        
        Parameters:
            name (str): Name of the variable.
            nullcline_function (function): Function describing the nullcline of the variable.
            parameters (dict): Parameters required by the derivative function.
            y_fun_x (Boolean) : wether the function is provided as y(x), according to the axis defined for each variable
        """
        
        mydict = {
            'nullcline_function': nullcline_function,
            'parameters': parameters,
            'y_fun_x': y_fun_x
        }    
        if name in self.nullclines.keys():
            self.nullclines[name].append(mydict)
        else:
            self.nullclines[name] = [mydict]
    
    def create_meshgrid_derivatives (self,n_X,n_Y,Xlim,Ylim,t):
        """
        Parameters
        ----------
        n_X : float
            number of points to evaluate in p axis.
        n_Y : float
            number of points to evaluate in  H axis.
        Xlim : tuple (float,float)
            limits to evaluate X.
        Ylim : tuple (float,float)
            limits to evaluate Y.


        Returns
        -------
        Xv, Yv : np.array (np.meshgrid)
        Xdot,Ydot : np.array (np.meshgrid - like)
            derivatives in each point 
        """
        Xv,Hv = np.meshgrid(np.linspace(Xlim[0],Xlim[1],n_X),np.linspace(Ylim[0],Ylim[1],n_Y))
        Xdot = np.empty_like(Xv)
        Ydot = np.empty_like(Hv)

        X_name = self.variable_x
        Y_name = self.variable_y
        for i in range(n_X):
            for j in range(n_Y):
                var_dict = {'t':t,X_name:Xv[i,j],Y_name:Hv[i,j]}
                derivatives = super().compute_derivative(var_dict)
                Ydot[i,j] = derivatives[Y_name]
                Xdot[i,j] = derivatives[X_name]
        return Xv,Hv,Xdot,Ydot
    
    
    def plot_nullclines (self,variable,xlim,ylim, fig = None, ax= None, color = None):
        flag_ret_figs = False
        if fig == None and ax == None:
            fig,ax = plt.subplots()
            flag_ret_figs = True
        
        for nullcline_dict in self.nullclines[variable]:
            f = nullcline_dict['nullcline_function']
            pars = nullcline_dict['parameters']

            y_function_x = nullcline_dict['y_fun_x']
            if y_function_x:
                x = np.linspace(xlim[0],xlim[1],1000)
                y = [f(_,pars) for _ in x]
                if color != None:
                    ax.plot(x,y,color = color)
                else:
                    ax.plot(x,y)
            else:
                x = np.linspace(ylim[0],ylim[1],1000)
                y = [f(_,pars) for _ in x]
                if color != None:
                    ax.plot(y,x, color = color)
                else:
                    ax.plot(y,x)
        if flag_ret_figs:
            return fig, ax
        
    
    def plot_streamplot (self, t,n_X,n_Y, xlim, ylim, fig=None, ax=None):
        xv,yv,xdot,ydot = self.create_meshgrid_derivatives(n_X,n_Y,xlim,ylim,t)        
        flag_ret_figs = False
        if fig == None and ax == None:
            fig,ax = plt.subplots()
            flag_ret_figs = True
        
        ax.streamplot(xv,yv,xdot,ydot,color = 'grey',density = 1)
        
        if flag_ret_figs:
            return fig, ax
    
    
    def plot_phase_portrait (self,t,n_X,n_Y, xlim, ylim,colors = None, fig = None, ax = None):
        flag_ret_figs = False

        if fig == None and ax == None:
            fig,ax = plt.subplots()
            flag_ret_figs = True
        variable_x = self.variable_x
        variable_y = self.variable_y
        self.plot_streamplot(t,n_X,n_Y,xlim,ylim,fig,ax)

        if colors == None:
            self.plot_nullclines(variable_x,xlim,ylim,fig = fig, ax = ax)
            self.plot_nullclines(variable_y,xlim,ylim,fig = fig, ax = ax)
        else:
            self.plot_nullclines(variable_x,xlim,ylim,fig = fig, ax = ax,color = colors[0])
            self.plot_nullclines(variable_y,ylim,ylim,fig = fig, ax = ax,color = colors[1])
        
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        if flag_ret_figs:
            return fig, ax
        
        
        
        
        
        
        
        