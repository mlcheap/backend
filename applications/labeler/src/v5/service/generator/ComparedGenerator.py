from .Generator import Generator
from src.v3.components.item import TaskObj
from src.v3.components.data import CompareImageData
from src.v3.components.label import Compare as CompareLabel


class CompareGenerator(Generator):
    def __init__(self, meta_model):
        super(CompareGenerator, self).__init__(meta_model)

    def generate_new_items(self, user_id, total_need_to_generate):
        return []


class RandomCompareGenerator(Generator):
    def __init__(self, meta_model):
        super(RandomCompareGenerator, self).__init__(meta_model)

    def generate_new_items(self, user_id, total_need_to_generate):
        items = []
        label = CompareLabel("attractiveness", "attractiveness?")
        while len(items) < total_need_to_generate:
            item = TaskObj(self.meta_model.project.project_name)
            im1 = self.meta_model.data.get_random_item()
            im2 = self.meta_model.data.get_random_item()
            if im1["_id"] != im2["_id"]:
                cim = CompareImageData(im1, im2, "images")
                item.add_part(cim)
                item.add_part(label)
            items.append(item)
        return items
