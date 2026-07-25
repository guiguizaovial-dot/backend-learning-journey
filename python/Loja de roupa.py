import tkinter as tk
from tkinter import messagebox, ttk

class LojaRoupasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento - Loja de Roupas")
        self.root.geometry("700x500")
        self.root.minsize(600, 400)

        # Base de dados em memória (Listas e Dicionários)
        self.clientes = []  # Lista de dicionários: {'codigo': str, 'nome': str}
        self.produtos = []  # Lista de dicionários: {'codigo': str, 'nome': str, 'preco': float, 'estoque': int}

        # Configuração da Interface
        self.criar_menu()
        self.criar_widgets_principais()

    def criar_menu(self):
        barra_menu = tk.Menu(self.root)
        
        # Menu Relatórios
        menu_relatorio = tk.Menu(barra_menu, tearoff=0)
        menu_relatorio.add_command(label="Inventário e Quantidades", command=self.exibir_relatorio_inventario)
        barra_menu.add_cascade(label="Relatórios", menu=menu_relatorio)

        self.root.config(menu=barra_menu)

    def criar_widgets_principais(self):
        # Notebook (Abas) para organizar as telas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Abas
        self.aba_cliente = ttk.Frame(self.notebook)
        self.aba_produto = ttk.Frame(self.notebook)
        self.aba_venda = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_cliente, text="Cadastrar Cliente")
        self.notebook.add(self.aba_produto, text="Cadastrar Produto")
        self.notebook.add(self.aba_venda, text="Realizar Venda")

        self.montar_formulario_cliente()
        self.montar_formulario_produto()
        self.montar_formulario_venda()

    def montar_formulario_cliente(self):
        frame = ttk.LabelFrame(self.aba_cliente, text="Dados do Cliente", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ttk.Label(frame, text="Código do Cliente:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_cli_cod = ttk.Entry(frame, width=30)
        self.entry_cli_cod.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.entry_cli_cod.focus()

        ttk.Label(frame, text="Nome Completo:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_cli_nome = ttk.Entry(frame, width=30)
        self.entry_cli_nome.grid(row=1, column=1, sticky=tk.W, pady=5)

        btn_cadastrar = ttk.Button(frame, text="Salvar Cliente", command=self.cadastrar_cliente)
        btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=15)

    def montar_formulario_produto(self):
        frame = ttk.LabelFrame(self.aba_produto, text="Dados do Produto", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ttk.Label(frame, text="Código do Produto:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_prod_cod = ttk.Entry(frame, width=30)
        self.entry_prod_cod.grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Nome da Peça:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_prod_nome = ttk.Entry(frame, width=30)
        self.entry_prod_nome.grid(row=1, column=1, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Preço Unitário (R$):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_prod_preco = ttk.Entry(frame, width=30)
        self.entry_prod_preco.grid(row=2, column=1, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Quantidade em Estoque:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_prod_estoque = ttk.Entry(frame, width=30)
        self.entry_prod_estoque.grid(row=3, column=1, sticky=tk.W, pady=5)

        btn_cadastrar = ttk.Button(frame, text="Salvar Produto", command=self.cadastrar_produto)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=15)

    def montar_formulario_venda(self):
        frame = ttk.LabelFrame(self.aba_venda, text="Efetuar Venda", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ttk.Label(frame, text="Código do Cliente:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_venda_cli = ttk.Entry(frame, width=30)
        self.entry_venda_cli.grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Código do Produto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_venda_prod = ttk.Entry(frame, width=30)
        self.entry_venda_prod.grid(row=1, column=1, sticky=tk.W, pady=5)

        ttk.Label(frame, text="Quantidade Desejada:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_venda_qtd = ttk.Entry(frame, width=30)
        self.entry_venda_qtd.grid(row=2, column=1, sticky=tk.W, pady=5)

        btn_vender = ttk.Button(frame, text="Concluir Venda", command=self.realizar_venda)
        btn_vender.grid(row=3, column=0, columnspan=2, pady=15)

    def cadastrar_cliente(self):
        codigo = self.entry_cli_cod.get().strip()
        nome = self.entry_cli_nome.get().strip()

        if not codigo or not nome:
            messagebox.showerror("Erro", "Preencha todos os campos do cliente!")
            return

        if any(c['codigo'] == codigo for c in self.clientes):
            messagebox.showerror("Erro", f"Já existe um cliente cadastrado com o código {codigo}!")
            return

        self.clientes.append({'codigo': codigo, 'nome': nome})
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        
        self.entry_cli_cod.delete(0, tk.END)
        self.entry_cli_nome.delete(0, tk.END)
        self.entry_cli_cod.focus()

    def cadastrar_produto(self):
        codigo = self.entry_prod_cod.get().strip()
        nome = self.entry_prod_nome.get().strip()
        preco_texto = self.entry_prod_preco.get().strip()
        estoque_texto = self.entry_prod_estoque.get().strip()

        if not codigo or not nome or not preco_texto or not estoque_texto:
            messagebox.showerror("Erro", "Preencha todos os campos do produto!")
            return

        try:
            preco = float(preco_texto)
            estoque = int(estoque_texto)
            if preco < 0 or estoque < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser numérico válido e estoque deve ser um número inteiro positivo!")
            return

        if any(p['codigo'] == codigo for p in self.produtos):
            messagebox.showerror("Erro", f"Já existe um produto cadastrado com o código {codigo}!")
            return

        self.produtos.append({
            'codigo': codigo,
            'nome': nome,
            'preco': preco,
            'estoque': estoque
        })
        
        messagebox.showinfo("Sucesso", f"Produto {nome} cadastrado com sucesso!")
        
        self.entry_prod_cod.delete(0, tk.END)
        self.entry_prod_nome.delete(0, tk.END)
        self.entry_prod_preco.delete(0, tk.END)
        self.entry_prod_estoque.delete(0, tk.END)
        self.entry_prod_cod.focus()

    def realizar_venda(self):
        codigo_cliente = self.entry_venda_cli.get().strip()
        codigo_produto = self.entry_venda_prod.get().strip()
        quantidade_texto = self.entry_venda_qtd.get().strip()

        if not codigo_cliente or not codigo_produto or not quantidade_texto:
            messagebox.showerror("Erro", "Preencha todos os campos para realizar a venda!")
            return

        # Validação do Cliente
        cliente_encontrado = next((c for c in self.clientes if c['codigo'] == codigo_cliente), None)
        if not cliente_encontrado:
            messagebox.showerror("Erro", f"Cliente com código {codigo_cliente} não encontrado!")
            return

        # Validação do Produto
        produto_encontrado = next((p for p in self.produtos if p['codigo'] == codigo_produto), None)
        if not produto_encontrado:
            messagebox.showerror("Erro", f"Produto com código {codigo_produto} não encontrado!")
            return

        try:
            quantidade_comprada = int(quantidade_texto)
            if quantidade_comprada <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "A quantidade da compra deve ser um número inteiro maior que zero!")
            return

        # Validação de Estoque Suficiente
        if produto_encontrado['estoque'] < quantidade_comprada:
            messagebox.showerror("Erro", f"Estoque insuficiente! Disponível apenas {produto_encontrado['estoque']} unidades.")
            return

        # Subtração de Estoque Precisa
        produto_encontrado['estoque'] -= quantidade_comprada
        valor_total = quantidade_comprada * produto_encontrado['preco']

        mensagem_sucesso = (
            f"Venda realizada com sucesso!\n\n"
            f"Cliente: {cliente_encontrado['nome']}\n"
            f"Produto: {produto_encontrado['nome']}\n"
            f"Quantidade: {quantidade_comprada}\n"
            f"Valor Total: R$ {valor_total:.2f}"
        )
        messagebox.showinfo("Sucesso", mensagem_sucesso)

        # Regra de Alerta de Estoque Mínimo (< 5 peças)
        if produto_encontrado['estoque'] < 5:
            aviso_estoque = (
                f"⚠️ ATENÇÃO: ESTOQUE BAIXO!\n\n"
                f"O produto '{produto_encontrado['nome']}' (Código: {produto_encontrado['codigo']}) "
                f"atingiu {produto_encontrado['estoque']} unidade(s) restante(s).\n"
                f"Realize um pedido urgente de reposição à central!"
            )
            messagebox.showwarning("Alerta de Estoque Mínimo", aviso_estoque)

        # Limpeza dos campos de venda
        self.entry_venda_cli.delete(0, tk.END)
        self.entry_venda_prod.delete(0, tk.END)
        self.entry_venda_qtd.delete(0, tk.END)
        self.entry_venda_cli.focus()

    def exibir_relatorio_inventario(self):
        if not self.produtos:
            messagebox.showinfo("Inventário", "Nenhum produto cadastrado na loja no momento.")
            return

        total_geral_itens = sum(p['estoque'] for p in self.produtos)
        
        relatorio_texto = f"--- RELATÓRIO DE INVENTÁRIO DA LOJA ---\n\n"
        for p in self.produtos:
            relatorio_texto += f"• Código: {p['codigo']} | Produto: {p['nome']}\n"
            relatorio_texto += f"  Preço: R$ {p['preco']:.2f} | Estoque Atual: {p['estoque']} un.\n"
            relatorio_texto += "-" * 40 + "\n"
        
        relatorio_texto += f"\nQuantidade Total de Produtos na Loja: {total_geral_itens} peça(s)"

        # Janela Pop-up para exibição do Relatório
        janela_relatorio = tk.Toplevel(self.root)
        janela_relatorio.title("Relatório de Inventário")
        janela_relatorio.geometry("450x400")

        texto_box = tk.Text(janela_relatorio, wrap=tk.WORD, padx=10, pady=10)
        texto_box.insert(tk.END, relatorio_texto)
        texto_box.config(state=tk.DISABLED)
        texto_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_fechar = ttk.Button(janela_relatorio, text="Fechar", command=janela_relatorio.destroy)
        btn_fechar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LojaRoupasApp(root)
    root.mainloop()
