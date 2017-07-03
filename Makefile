VENV_BIN_DIR:="venv/bin"
DEPS:="requirements.txt"
PIP:="$(VENV_BIN_DIR)/pip"

define create-venv
python3.5 -m venv venv
endef

venv:
	@$(create-venv)
	@$(PIP) install -U pip -q
	@$(PIP) install -r $(DEPS)
