from dbt.adapters.base import Column


class CrateDBColumn(Column):
    @property
    def data_type(self):
        # on cratedb, do not convert 'text' or 'varchar' to 'varchar()'
        if self.dtype.lower() == "text" or (
            self.dtype.lower() == "character varying" and self.char_size is None
        ):
            return self.dtype
        return super().data_type
