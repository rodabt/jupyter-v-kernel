from ipykernel.kernelapp import IPKernelApp
from .kernel import VKernel
IPKernelApp.launch_instance(kernel_class=VKernel)
