import pprint

class Config():

    def __init__(self, **kwargs):

        self.data_path = '/content/drive/MyDrive/fcsn_tvsum.h5'
        self.save_dir = '/content/save_dir'
        self.score_dir = '/content/score_dir'

        self.n_epochs = 50
        self.batch_size = 5

        for a,b in kwargs.items():
            setattr(self,a,b)

    def __repr__(self):

        config_str = 'Configurations\n' + pprint.pformat(self.__dict__)

        return config_str

if __name__ == '__main__':
    config = Config()
    print(config)
