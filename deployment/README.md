minikubeで動かす

minikube start

```
minikube start --driver=docker
```

imageをminikubeにload

```bash
minikube load <image-name>:<tag>
```

manifest を apply

```bash
kubectl apply -f <manifest>
```

minikube service

```bash
minikube service <service-name> --url
```

manifest を delete


```bash
kubectl delete -f <manifest>
```