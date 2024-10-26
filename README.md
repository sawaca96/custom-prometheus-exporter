https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack

docker build . -t myapp:dev

kubectl get secret grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
